import "../styles/cssreset.css"
import 'rsuite/dist/rsuite.min.css';
import '../styles/globals.css'
import React, { useState } from "react";
import type { AppProps } from 'next/app'

function MyApp({ Component, pageProps }: AppProps) {

  return (
    <Component {...pageProps} />
  )
}

export default MyApp
