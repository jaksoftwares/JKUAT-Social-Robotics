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
        'custom-lightBlue': '#669ACC',
        'custom-lightGray': '#ECEDF2',
        'custom-gray': '#D9D9D9',
        'custom-darkGray': '#676767',
      },
    },
  },
  plugins: [],
};
