import React from "react";

import { Sidenav, Nav } from "rsuite";

import apiRoutes from "../../utils/apiRoutes";

const Drawer: React.FC = () => {
    return (
        <Sidenav defaultOpenKeys={["3", "4"]}>
          <Sidenav.Body>
            <Nav activeKey="1">
              <Nav.Menu eventKey="3" title="API Routes">
                {apiRoutes.map((apiRoute, index) => <Nav.Item key={index} eventKey={`0-${index}`}>[{apiRoute.type}] {apiRoute.title}</Nav.Item>)}
              </Nav.Menu>
            </Nav>
          </Sidenav.Body>
        </Sidenav>
    )
};

export default Drawer;
