import React from "react";

import Navbar from "../navbar";
import Footer from "../footer";

interface Props {
  children: React.ReactNode;
}

const Layout: React.FC<Props> = ({ children }) => {
  return (
    <div className="bg-background flex flex-col justify-between h-full">
      <Navbar />

      {children}

      <Footer />
    </div>
  );
};

export default Layout;
