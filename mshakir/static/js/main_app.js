// Main Showcase Home Page

const date = new Date();
const year = document.getElementById('year');
year.innerHTML = date.getFullYear();

// Type Writing Effect Using Pure Vanilla JavaScript

class TypeWriter {
  constructor(txtElement, words, wait = 500) {
    this.txtElement = txtElement;
    this.words = words;
    this.txt = '';
    this.wordIndex = 0;
    this.wait = parseInt(wait, 10);
    this.type();
    this.isDeleting = false;
  }

  type() {
    // Current index of word
    const current = this.wordIndex % this.words.length;
    // Get full text of current word
    const fullTxt = this.words[current];

    // Check if deleting
    if (this.isDeleting) {
      // Remove char
      this.txt = fullTxt.substring(0, this.txt.length - 1);
    } else {
      // Add char
      this.txt = fullTxt.substring(0, this.txt.length + 1);
    }

    // Insert txt into element
    this.txtElement.innerHTML = `<span class="txt">${this.txt}</span>`;

    // Initial Type Speed
    let typeSpeed = 100;

    if (this.isDeleting) {
      typeSpeed /= 2;
    }

    // If word is complete
    if (!this.isDeleting && this.txt === fullTxt) {
      // Make pause at end
      typeSpeed = this.wait;
      // Set delete to true
      this.isDeleting = true;
    } else if (this.isDeleting && this.txt === '') {
      this.isDeleting = false;
      // Move to next word
      this.wordIndex++;
      // Pause before start typing
      typeSpeed = 200;
    }

    setTimeout(() => this.type(), typeSpeed);
  }
}


// Init On DOM Load
document.addEventListener('DOMContentLoaded', init);

// Init App
function init() {
  const txtElement = document.querySelector('.txt-type');
  const words = JSON.parse(txtElement.getAttribute('data-words'));
  const wait = txtElement.getAttribute('data-wait');
  // Init TypeWriter
  new TypeWriter(txtElement, words, wait);
}



// For Footer To change the Year dynamically




// Constructor is basically runs when object is instantiated
// Instead of creating a prototype we can create a funciton inside the class

////////////////////////////////////////////////////////////////
// const current = document.getElementById('current');
// // To Select all the images
// const imgs = document.querySelectorAll(' .imgs img');
// const opacity = 0.3;
// imgs[0].style.opacity = opacity;
// imgs.forEach(function (img) {
//   console.log(img);
//   img.addEventListener('click', showImages);
// });

// function showImages(e) {
//   console.log("Show Images Is Connected Now");
//   // Reset the Opacity.
//   imgs.forEach(img => (img.style.opacity = 1));
//   // Change the Current image for each Click
//   current.src = e.target.src;

//   // Add the animation fadeIn
//   current.classList.add('fade-in');
//   setTimeout(function () {
//     current.classList.remove('fade-in');
//   }, 500)

//   //change the opacity
//   e.target.style.opacity = opacity;
// }