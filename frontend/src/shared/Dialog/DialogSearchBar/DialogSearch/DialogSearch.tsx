import React from 'react';
import styles from './dialogsearch.module.css';

export function DialogSearch() {
  return (
    <form className={styles.form}>
      <input className={styles.input} type="text" placeholder="введите запрос" />
    </form>
  );
}
