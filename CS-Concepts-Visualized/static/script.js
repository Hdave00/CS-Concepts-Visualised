document.addEventListener('DOMContentLoaded', function () {

    // csrf token 
    const csrfToken = document.querySelector('input[name="csrf_token"]').value;

    const sections = document.querySelectorAll('.section');
    let score = 0;

    sections.forEach((section, index) => {
        const feedback = section.querySelector(`.feedback${index + 1}`);
        const correct = section.querySelector('.correct');
        const incorrects = section.querySelectorAll('.incorrect');

        correct.addEventListener('click', () => {
            correct.style.backgroundColor = 'green';
            feedback.innerHTML = 'Correct!';
            score++;
            console.log(`Score: ${score}`);
        });

        incorrects.forEach(button => {
            button.addEventListener('click', () => {
                button.style.backgroundColor = 'red';
                feedback.innerHTML = 'Incorrect';
            });
        });
    });

    // submitting the results
    function submitScore() {
        fetch('/submit_score', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
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

    // Create and append the submit button
    const submitButton = document.createElement('button');
    submitButton.textContent = 'Submit Quiz';
    submitButton.classList.add('submit-button');
    submitButton.addEventListener('click', submitScore);
    document.body.appendChild(submitButton);
});