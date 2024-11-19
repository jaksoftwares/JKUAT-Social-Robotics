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
        'custom-lintingGreenDark': '#94C83D',
        'custom-cyanBlue': '#7CCBF2', 
        'custom-red': '#FF0000',
        'custom-lightGray': '#ECEDF2',
        'custom-gray': '#D9D9D9',
        'custom-darkGray': '#676767',
      },
    },
  },
  plugins: [],
};