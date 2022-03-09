import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'noTweets',
})
export class NoTweetsPipe implements PipeTransform {
  transform(value: number): string {
    if (isNaN(value)) {
      return '';
    } else if (value < 1000) {
      return value + ' Tweet';
    } else if (value < 10000) {
      let valueStr = value.toString();
      return valueStr.slice(0, 1) + '.' + valueStr.slice(1) + ' Tweet';
    } else if (value < 100000) {
      let valueStr = value.toString();
      return valueStr.slice(0, 2) + '.' + valueStr.slice(2, 3) + ' χιλ. Tweet';
    } else if (value < 1000000) {
      let valueStr = value.toString();
      return valueStr.slice(0, 3) + '.' + valueStr.slice(3, 4) + ' χιλ. Tweet';
    } else {
      return "Εκατ. Tweet απ' όλο τον κόσμο";
    }
  }
}
