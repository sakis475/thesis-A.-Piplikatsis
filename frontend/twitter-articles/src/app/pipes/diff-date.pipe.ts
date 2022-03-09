import { Pipe, PipeTransform } from '@angular/core';
import { of } from 'rxjs';

@Pipe({
  name: 'diffDate',
})
export class DiffDatePipe implements PipeTransform {
  transform(value: any): any {
    value = value.trim();

    let formatDateDiff = value.split(' ');

    let prinMeta = formatDateDiff[0];
    let daysNum = formatDateDiff[0];

    if (prinMeta.slice(0, 1) == '-') {
      prinMeta = 'πριν';
      daysNum = daysNum.slice(1, 2);
    } else {
      prinMeta = 'μετα';
      daysNum = daysNum.slice(0, 1);
    }

    let minusPlusDays = formatDateDiff[2].slice(0, 1);
  }
}
