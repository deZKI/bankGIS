import React from 'react';
import styles from './dialog.module.css';
import {DialogSearchBar} from "./DialogSearchBar";
import {DialogOptions} from "./DialogOptions";
import {DialogAddresses} from "./DialogAddresses";

export function Dialog() {
  return (
    <div className={styles.container}>
      <DialogSearchBar />
      <DialogOptions />
      <DialogAddresses />
    </div>
  );
}
