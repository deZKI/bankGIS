import React, {useEffect} from 'react';
import styles from './mapgl.module.css';
import {load} from '@2gis/mapgl';
import {MapWrapper} from "../MapWrapper";

export const MAP_CENTER = [37.6156, 55.7522];

export function Mapgl() {
  useEffect(() => {
    let map: mapgl.Map | undefined = undefined;

    load().then((mapgl) => {
      map = new mapgl.Map('map-container', {
        center: MAP_CENTER,
        zoom: 13,
        key: 'a1893935-6834-4445-b97a-3405fb426c5b',
        style: 'e05ac437-fcc2-4845-ad74-b1de9ce07555'
      });
    });
  }, []);

  return (
    <MapWrapper />
  );
}
