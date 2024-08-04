/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.{html,js}',
  ],
  theme: {
    extend: {
      fontFamily: {
        raleway: ['Raleway', 'sans-serif'],
        lato: ['Lato', 'sans-serif'],
        martel: ['Martel Sans', 'sans-serif'],
      },
      colors: {
        'custom-navyBlue': '#003B6D',
        'Custom-lightBlue': '#669ACC',
        'Custom-lightGray': '#ECEDF2',
        'Custom-gray': '#BDBDBD',
        'Custom-darkGray': '#676767',
      },
    },
  },
  plugins: [],
};
