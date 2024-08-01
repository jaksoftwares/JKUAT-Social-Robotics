/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.{html,js}',
  ],
  theme: {
    extend: {},
    fontFamily: {
      raleway: ['Raleway','sans-serif'],
      lato: ['Lato','sans-serif'],
      'martel': ['Martel Sans','sans-serif'],

    },
    colors:{
      'custom-green': '#95cb48',
      },
  },
  plugins: [],
};
