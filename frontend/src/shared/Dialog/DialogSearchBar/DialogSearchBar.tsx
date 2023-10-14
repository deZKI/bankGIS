import React from 'react';
import styles from './dialogsearchbar.module.css';
import {DialogSearch} from "./DialogSearch";
import {DialogFilters} from "./DialogFilters";

export function DialogSearchBar() {
  return (
    <div className={styles.container}>
      <DialogSearch />
      <DialogFilters />
    </div>
  );
}
