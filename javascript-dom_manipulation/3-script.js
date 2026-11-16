const myHeader = document.getElementById('toggle_header');

myHeader.addEventListener('click', redFunction);

const toggleHeader = document.querySelector('header');

function redFunction () {
  toggleHeader.classList.toggle('red');
  toggleHeader.classList.toggle('green');
}
