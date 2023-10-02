import React from 'react';
import './main.global.css';
import {Layout} from "./shared/Layout";
import {Content} from "./shared/Content";

function AppComponent() {
  return (
    <Layout>
      <Content>
        <div>Hello world!</div>
      </Content>
    </Layout>
  );
}

export const App = () => <AppComponent />
