async function helloSalut () {
  try {
    const response = await fetch('https://hellosalut.stefanbohacek.com/?lang=fr');
    if (response.ok) {
      const data = await response.json();

      const helloElement = document.getElementById('hello');
      helloElement.innerHTML = data.hello;
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

helloSalut();
