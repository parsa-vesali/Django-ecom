// Select DOM elements
const nav = document.querySelector('.mobile-menu');
const openNavBtn = document.querySelector('.mobile-menu__open-icon');
const closeNavBtn = document.querySelector('.mobile-menu__close-icon');
const openSubmenuBtn = document.querySelector('.open-submenu');
const submenu = document.querySelector('.submenu');
const arrowsubmenu = document.querySelector('.arrow-submenu');
const overlay = document.querySelector('.overlay');
const openShoppingCartButtons = document.querySelectorAll('.open-shopping-cart__btn');
const shoppingCart = document.querySelector('.shopping-cart');
const closeShoppingCartButtons = document.querySelectorAll('.close-shopping-cart__btn');
const alertElem = document.querySelector('.top-alert');
const alertBtnElem = document.querySelector('.close-alert-btn');
const toggleThemeBtns = document.querySelectorAll('.toggle-theme');

// Function to open mobile menu
const openNav = () => {
  overlay.classList.remove('hidden');
  overlay.classList.add('flex');
  nav.classList.remove('-right-64');
  nav.classList.add('right-0');
};

// Function to close mobile menu
const closeNav = () => {
  overlay.classList.add('hidden');
  overlay.classList.remove('flex');
  nav.classList.remove('right-0');
  nav.classList.add('-right-64');
};

// Function to toggle submenu
const toggleSubmenu = () => {
  openSubmenuBtn.classList.toggle('text-blue-500');
  submenu.classList.toggle('hidden');
  submenu.classList.toggle('flex');
  arrowsubmenu.classList.toggle('-rotate-90');
};


// Event listener for opening mobile menu
openNavBtn.addEventListener('click', openNav);

// Event listener for overlay click to close mobile menu and shopping cart
overlay.addEventListener('click', () => {
  closeNav();
});


// Event listener for closing mobile menu
closeNavBtn.addEventListener('click', closeNav);

// Event listener for submenu toggle
openSubmenuBtn.addEventListener('click', toggleSubmenu);


// Custom Input Fields with Increment/Decrement Buttons
document.addEventListener('DOMContentLoaded', () => {
  // Event Listener for Increment Buttons
  document.querySelectorAll('.increment').forEach(button => {
    button.addEventListener('click', event => {
      const input = event.target.closest('button').querySelector('.custom-input');
      const value = parseInt(input.value) || 0;
      if (value < 20) {
        input.value = value + 1;
      }
    });
  });

  // Event Listener for Decrement Buttons
  document.querySelectorAll('.decrement').forEach(button => {
    button.addEventListener('click', event => {
      const input = event.target.closest('button').querySelector('.custom-input');
      const value = parseInt(input.value) || 0;
      if (value > 0) {
        input.value = value - 1;
      }
    });
  });
});