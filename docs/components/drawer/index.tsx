import React from "react";
import Link from "next/link";

import { Sidenav, Nav } from "rsuite";

import apiRoutes from "../../utils/apiRoutes";

// @ts-ignore
const NavLink = React.forwardRef(({ href, as, ...rest }, ref) => (
  <Link href={href} as={as}>
    {/* @ts-ignore */}
    <a ref={ref} {...rest} />
  </Link>
));
NavLink.displayName = "NavLink"

const Drawer: React.FC = () => {
    return (
        <Sidenav defaultOpenKeys={["3", "4"]}>
          <Sidenav.Body>
            <Nav activeKey="1">
              <Nav.Item as={NavLink} href="/home">Home</Nav.Item>
              <Nav.Menu eventKey="3" title="API Routes">
                {apiRoutes.map((apiRoute, index) => (
                    <Nav.Item as={NavLink} href={`/${apiRoute.id}`} key={index} eventKey={`0-${index + 1}`}> 
                      <span className={`font-bold ${ apiRoute.type === "GET" ? "text-highlight" : "text-tertiary" }`}>[{apiRoute.type}]</span> <span>{apiRoute.title}</span>
                    </Nav.Item>
                ))}
              </Nav.Menu>
            </Nav>
          </Sidenav.Body>
        </Sidenav>
    )
};

export default Drawer;
