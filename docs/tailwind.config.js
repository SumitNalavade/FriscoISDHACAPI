/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        "background" : "#fffffe",
        "headline" : "#094067",
        "headline-darker": "#60aedb",
        "paragraph" : "#5f6c7b",
        "button" : "#3da9fc",
        "button-text": "#fffffe",
        "stroke" : "#094067",
        "main" : "#fffffe",
        "highlight" : "#3da9fc",
        "secondary" : '#90b4ce',
        "tertiary" : "#ef4565"
      }
    },
  },
  plugins: [],
}
