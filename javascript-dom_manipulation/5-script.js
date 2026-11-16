const updateHeaderBtn = document.getElementById('update_header');
const headerElement = document.querySelector('header');

updateHeaderBtn.addEventListener('click', updateHeader);

function updateHeader () {
  headerElement.innerHTML = 'New Header!!!';
}
