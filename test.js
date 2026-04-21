import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  stages: [
    { duration: '30s', target: 20 },  // ramp up
    { duration: '1m', target: 50 },   // steady load
    { duration: '30s', target: 0 },   // ramp down
  ],
};

export default function () {
  http.get('http://<13.206.123.40>');
  sleep(1);
}
