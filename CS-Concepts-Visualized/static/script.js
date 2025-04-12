// the JS logic for the quiz page that handles button submission, checks if the answer is right or wrong and tallies the score
// also contains the submit score function that redirects the user to the scores page (works with the app route in flask)

document.addEventListener('DOMContentLoaded', function() {
    let score = 0;

    // Example for the first question
    let correct1 = document.querySelector('.section:nth-of-type(1) .correct');
    correct1.addEventListener('click', function() {
        correct1.style.backgroundColor = 'green';
        document.querySelector('.section:nth-of-type(1) .feedback1').innerHTML = 'Correct!';
        score++;
        console.log("Score: " + score);
    });

    let incorrects1 = document.querySelectorAll('.section:nth-of-type(1) .incorrect');
    for (let i = 0; i < incorrects1.length; i++) {
        incorrects1[i].addEventListener('click', function() {
            incorrects1[i].style.backgroundColor = 'Red';
            incorrects1[i].parentElement.querySelector('.feedback1').innerHTML = 'Incorrect';
        });
    }

    // Second question
    let correct2 = document.querySelector('.section:nth-of-type(2) .correct');
    correct2.addEventListener('click', function() {
        correct2.style.backgroundColor = 'green';
        document.querySelector('.section:nth-of-type(2) .feedback2').innerHTML = 'Correct!';
        score++;
        console.log("Score: " + score);
    });

    let incorrects2 = document.querySelectorAll('.section:nth-of-type(2) .incorrect');
    for (let i = 0; i < incorrects2.length; i++) {
        incorrects2[i].addEventListener('click', function() {
            incorrects2[i].style.backgroundColor = 'Red';
            incorrects2[i].parentElement.querySelector('.feedback2').innerHTML = 'Incorrect';
        });
    }

    // Third question
    let correct3 = document.querySelector('.section:nth-of-type(3) .correct');
    correct3.addEventListener('click', function() {
        correct3.style.backgroundColor = 'green';
        document.querySelector('.section:nth-of-type(3) .feedback3').innerHTML = 'Correct!';
        score++;
        console.log("Score: " + score);
    });

    let incorrects3 = document.querySelectorAll('.section:nth-of-type(3) .incorrect');
    for (let i = 0; i < incorrects3.length; i++) {
        incorrects3[i].addEventListener('click', function() {
            incorrects3[i].style.backgroundColor = 'Red';
            incorrects3[i].parentElement.querySelector('.feedback3').innerHTML = 'Incorrect';
        });
    }

    // Fourth question
    let correct4 = document.querySelector('.section:nth-of-type(4) .correct');
    correct4.addEventListener('click', function() {
        correct4.style.backgroundColor = 'green';
        document.querySelector('.section:nth-of-type(4) .feedback4').innerHTML = 'Correct!';
        score++;
        console.log("Score: " + score);
    });

    let incorrects4 = document.querySelectorAll('.section:nth-of-type(4) .incorrect');
    for (let i = 0; i < incorrects4.length; i++) {
        incorrects4[i].addEventListener('click', function() {
            incorrects4[i].style.backgroundColor = 'Red';
            incorrects4[i].parentElement.querySelector('.feedback4').innerHTML = 'Incorrect';
        });
    }

    // Fifth question
    let correct5 = document.querySelector('.section:nth-of-type(5) .correct');
    correct5.addEventListener('click', function() {
        correct5.style.backgroundColor = 'green';
        document.querySelector('.section:nth-of-type(5) .feedback5').innerHTML = 'Correct!';
        score++;
        console.log("Score: " + score);
    });

    let incorrects5 = document.querySelectorAll('.section:nth-of-type(5) .incorrect');
    for (let i = 0; i < incorrects5.length; i++) {
        incorrects5[i].addEventListener('click', function() {
            incorrects5[i].style.backgroundColor = 'Red';
            incorrects5[i].parentElement.querySelector('.feedback5').innerHTML = 'Incorrect';
        });
    }

    // question 6
    let correct6 = document.querySelector('.section:nth-of-type(6) .correct');
    correct6.addEventListener('click', function() {
        correct6.style.backgroundColor = 'green';
        document.querySelector('.section:nth-of-type(6) .feedback6').innerHTML = 'Correct!';
        score++;
        console.log("Score: " + score);
    });

    let incorrects6 = document.querySelectorAll('.section:nth-of-type(6) .incorrect');
    for (let i = 0; i < incorrects6.length; i++) {
        incorrects6[i].addEventListener('click', function() {
            incorrects6[i].style.backgroundColor = 'Red';
            incorrects6[i].parentElement.querySelector('.feedback6').innerHTML = 'Incorrect';
        });
    }

    // question 7
    let correct7 = document.querySelector('.section:nth-of-type(7) .correct');
    correct7.addEventListener('click', function() {
        correct7.style.backgroundColor = 'green';
        document.querySelector('.section:nth-of-type(7) .feedback7').innerHTML = 'Correct!';
        score++;
        console.log("Score: " + score);
    });

    let incorrects7 = document.querySelectorAll('.section:nth-of-type(7) .incorrect');
    for (let i = 0; i < incorrects7.length; i++) {
        incorrects7[i].addEventListener('click', function() {
            incorrects7[i].style.backgroundColor = 'Red';
            incorrects7[i].parentElement.querySelector('.feedback7').innerHTML = 'Incorrect';
        });
    }

    // question 8
    let correct8 = document.querySelector('.section:nth-of-type(8) .correct');
    correct8.addEventListener('click', function() {
        correct8.style.backgroundColor = 'green';
        document.querySelector('.section:nth-of-type(8) .feedback8').innerHTML = 'Correct!';
        score++;
        console.log("Score: " + score);
    });

    let incorrects8 = document.querySelectorAll('.section:nth-of-type(8) .incorrect');
    for (let i = 0; i < incorrects8.length; i++) {
        incorrects8[i].addEventListener('click', function() {
            incorrects8[i].style.backgroundColor = 'Red';
            incorrects8[i].parentElement.querySelector('.feedback8').innerHTML = 'Incorrect';
        });
    }

    // question 9
    let correct9 = document.querySelector('.section:nth-of-type(9) .correct');
    correct9.addEventListener('click', function() {
        correct9.style.backgroundColor = 'green';
        document.querySelector('.section:nth-of-type(9) .feedback9').innerHTML = 'Correct!';
        score++;
        console.log("Score: " + score);
    });

    let incorrects9 = document.querySelectorAll('.section:nth-of-type(9) .incorrect');
    for (let i = 0; i < incorrects9.length; i++) {
        incorrects9[i].addEventListener('click', function() {
            incorrects9[i].style.backgroundColor = 'Red';
            incorrects9[i].parentElement.querySelector('.feedback9').innerHTML = 'Incorrect';
        });
    }

    // question 10
    let correct10 = document.querySelector('.section:nth-of-type(10) .correct');
    correct10.addEventListener('click', function() {
        correct10.style.backgroundColor = 'green';
        document.querySelector('.section:nth-of-type(10) .feedback10').innerHTML = 'Correct!';
        score++;
        console.log("Score: " + score);
    });

    let incorrects10 = document.querySelectorAll('.section:nth-of-type(10) .incorrect');
    for (let i = 0; i < incorrects10.length; i++) {
        incorrects10[i].addEventListener('click', function() {
            incorrects10[i].style.backgroundColor = 'Red';
            incorrects10[i].parentElement.querySelector('.feedback10').innerHTML = 'Incorrect';
        });
    }

    // function to submit the score, this will send data back to the app.py for use in updating our database
    function submitScore() {
        fetch('/submit_score', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ score: score })
        })
        .then(response => {
            if (response.redirected) {
                window.location.href = response.url;
            } else {
                return response.json();
            }
        })
        .then(data => {
            console.log('Success:', data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    }

    // call submitScore when the quiz is completed
    // there is a button to submit the quiz which is then
    let submitButton = document.createElement('button');
    submitButton.textContent = 'Submit Quiz';
    submitButton.addEventListener('click', submitScore);
    document.body.appendChild(submitButton);
});
