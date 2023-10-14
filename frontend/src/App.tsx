import React from 'react';
import './main.global.css';
import {Dialog} from "./shared/Dialog";
import {Mapgl} from "./shared/Mapgl";

function AppComponent() {
  return (
    <div style={{ width: "100%", height: "100vh" }}>
      <Dialog />
      <Mapgl />
    </div>
  );
}

export const App = () => <AppComponent />
