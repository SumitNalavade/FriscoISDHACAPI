import React from "react";
import Head from 'next/head'

import Navbar from "../navbar";

interface Props {
  children: React.ReactNode;
}

const Layout: React.FC<Props> = ({ children }) => {
  return (
    <>
    <Head>
      <title>Frisco ISD HAC API</title>
      <meta name="description" content="REST API to access student data from Home Access Center (Frisco ISD) "></meta>
      <meta name="viewport" content="width=device-width, initial-scale=1" />
    </Head>
      <div className="bg-background flex flex-col h-full text-paragraph">
        <Navbar />

        {children}
      </div>
    </>
  );
};

export default Layout;
