document.addEventListener('DOMContentLoaded', () => {
    const card = document.querySelector('.card');

    card.addEventListener('click', () => {
        card.classList.toggle('is-flipped');
    });
});
