import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'similarity',
})
export class SimilarityPipe implements PipeTransform {
  transform(value: number): string {
    if (isNaN(value)) {
      return 'error';
    } else if (value < 19) {
      return 'ΜΗ-ΣΧΕΤΙΚΟ';
    } else if (value < 35) {
      return 'ΛΙΓΟ-ΣΧΕΤΙΚΟ';
    } else if (value < 100) {
      return 'ΣΧΕΤΙΚΟ';
    } else if (value < 150) {
      return 'ΠΟΛΥ-ΣΧΕΤΙΚΟ';
    } else {
      return 'ΕΞΑΙΡΕΤΙΚΑ-ΣΧΕΤΙΚΟ';
    }
  }
}
