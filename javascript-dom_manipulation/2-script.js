const myHeader = document.getElementById('red_header');

myHeader.addEventListener('click', redFunction);

function redFunction () {
  document.querySelector('header').classList.add('red');
}
