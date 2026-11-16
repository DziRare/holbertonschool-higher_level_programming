const addItemElement = document.getElementById('add_item');

addItemElement.addEventListener('click', addItem);

function addItem () {
  const listItem = document.createElement('li');
  listItem.innerHTML = 'Item';
  document.getElementsByClassName('my_list')[0].appendChild(listItem);
}
