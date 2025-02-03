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

      animation: {
        'fade-in': 'fadeIn 1s ease-in-out forwards',
        'fade-in-delay': 'fadeIn 1s ease-in-out 0.5s forwards', // Delay second section
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: 0, transform: 'translateY(20px)' },
          '100%': { opacity: 1, transform: 'translateY(0)' },
        },
      },
    },
  },
  plugins: [],
};
