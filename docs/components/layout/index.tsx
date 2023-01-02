import React from "react";

import Navbar from "../navbar";

interface Props {
  children: React.ReactNode;
}

const Layout: React.FC<Props> = ({ children }) => {
  return (
    <div className="bg-background flex flex-col h-full text-paragraph">
      <Navbar />

      {children}
    </div>
  );
};

export default Layout;
