import React from 'react';
import styles from './dialogoptions.module.css';

export function DialogOptions() {
  return (
    <ul className={styles.list}>
      <li className={styles.item}>
        <button className={styles.button}>
          <span className={styles.desc}>оформить кредит</span>
        </button>
      </li>
      <li className={styles.item}>
        <button className={styles.button}>
          <span className={styles.desc}>открыть вклад</span>
        </button>
      </li>
      <li className={styles.item}>
        <button className={styles.button}>
          <span className={styles.desc}>выпустить карту</span>
        </button>
      </li>
      <li className={styles.item}>
        <button className={styles.button}>
          <span className={styles.desc}>оформить карту</span>
        </button>
      </li>
      <li className={styles.item}>
        <button className={styles.button}>
          <span className={styles.desc}>открыть брокерский счет</span>
        </button>
      </li>
    </ul>
  );
}
