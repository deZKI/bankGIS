import React from 'react';
import styles from './dialogfilters.module.css';
import {FiltersIcon} from "../../../Icons/FiltersIcon";

export function DialogFilters() {
  return (
    <button className={styles.icon}>
      <FiltersIcon />
    </button>
  );
}
