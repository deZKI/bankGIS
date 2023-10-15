import React from 'react';
import './main.global.css';
import {Dialog} from "./shared/Dialog";
import {Mapgl} from "./shared/Mapgl";
import {rootReducer} from "./store/reducer";
import {composeWithDevTools} from "redux-devtools-extension";
import {applyMiddleware, createStore} from "redux";
import thunk from "redux-thunk";
import {Provider} from "react-redux";
import {useBankBranchesData} from "./hooks/useBankBranchesData";

const store = createStore(rootReducer, composeWithDevTools(
  applyMiddleware(thunk)
));

function AppComponent() {
  const bankBranches = useBankBranchesData();
  console.log(bankBranches);

  return (
    <div style={{ width: "100%", height: "100vh" }}>
      <Dialog />
      <Mapgl />
    </div>
  );
}

export const App = () => 
  <Provider store={store}>
    <AppComponent />
  </Provider>
;
