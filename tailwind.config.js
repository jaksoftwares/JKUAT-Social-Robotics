/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.{html,js}',
  ],
  theme: {
    extend: {},
    fontFamily: {
      raleway: ['Raleway', 'sans-serif'],
      lato: ['Lato', 'sans-serif'],
    },
    colors: {
      'custom-green': '#95CB48',
      'Custom-Gray': '#B3B3B3',
      'Custom-red': '#ff0000',

    },
  },
  plugins: [],
};
