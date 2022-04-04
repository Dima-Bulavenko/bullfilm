const ratings = document.querySelectorAll('.rating')
if (ratings.length > 0) {
    initRatings();
}

//Main function
function initRatings() {
    // 'Run' by all ratings on a page
    let ratingActive, ratingValue;
    for (let index = 0; index < ratings.length; index++) {
        const rating = ratings[index];
        initRating(rating);
    }
    //Initialization special rating
    function initRating(rating) {
        initRatingVars(rating);

        setRatingsActiveWidth();
        if (rating.classList.contains('rating_set')) {
            setRating(rating);
        }
    }

    //Initialization variables
    function initRatingVars(rating) {
        ratingActive = rating.querySelector('.rating_active');
        ratingValue = rating.querySelector('.rating_value');
    }
    //Changing wight active stars
    function setRatingsActiveWidth(index = ratingValue.innerHTML.replace(',', '.')) {
        const ratingActiveWidth = index / 0.1;
        ratingActive.style.width = `${ratingActiveWidth}%`;
    }

    //opportunity to set rating
    function setRating(rating) {
        const ratingItems = rating.querySelectorAll('.rating_item');
        for (let index = 0; index < ratingItems.length; index++) {
            const ratingItem = ratingItems[index];
            ratingItem.addEventListener('mouseenter', function (e) {
                // updating variables
                initRatingVars(rating);
                // updating active stars
                setRatingsActiveWidth(ratingItem.value);
            });

            ratingItem.addEventListener('mouseleave', function (e) {
                // updating active stars
                setRatingsActiveWidth();
            });
            ratingItem.addEventListener('click', function (e) {
                // updating variables
                initRatingVars(rating);
                if (rating.dataset.ajax) {
                    // send to server
                    setRatingValue(ratingItem.value, rating);
                } else {
                    // display pointed rating
                    ratingValue.innerHTML = index + 1;
                    setRatingsActiveWidth();
                }
            });


        }
    }

    async function setRatingValue(value, rating) {
        if (!rating.classList.contains('rating_sending')) {
            rating.classList.add('rating_sending');
            let film_name
            if (rating.getElementsByClassName('rating_video').length > 0) {
                film_name = document.getElementById('film_name').textContent;
            } else {
                film_name = rating.closest(".content_box").querySelector("p").textContent;
            }

            function getCookie(name) {
                console.log(document.cookie)
                let cookieValue = null;
                if (document.cookie && document.cookie !== '') {
                    const cookies = document.cookie.split(';');
                    for (let i = 0; i < cookies.length; i++) {
                        const cookie = cookies[i].trim();
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) === (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }

            const csrftoken = getCookie('csrftoken');
            // sending data to server
            let response = await fetch('http://127.0.0.1:8000/ajax/', {
                method: 'POST',
                body: JSON.stringify({
                    userRating: Number(value),
                    film_name: film_name
                }),
                headers: {
                    "X-CSRFToken": csrftoken

                },
            });
            if (response.ok) {
                const result = await response.json();
                if (rating.getElementsByClassName('rating_video').length > 0) {
                    const amountVotersValue = rating.querySelector('.amount_voters');
                    const newAmountVoters = result.amount_voters;
                    amountVotersValue.innerHTML = newAmountVoters;
                }


                // get new rating
                const newRating = String(Math.round(result.videoRating * 10) / 10).replace('.', ',');

                // output new middle result
                ratingValue.innerHTML = newRating;

                // update active stars
                setRatingsActiveWidth();

                rating.classList.remove('rating_sending');
            } else {
                alert('Error');
                rating.classList.remove('rating_sending');
            }
        }
    }
}