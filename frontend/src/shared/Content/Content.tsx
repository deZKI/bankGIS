import React, {ReactNode} from 'react';
import styles from './content.module.css';

interface IContent {
  children?: ReactNode;
}

export function Content({ children }: IContent) {
  return (
    <div className={styles.content}>
      {children}
    </div>
  );
}
