#!/usr/bin/node
exports.nb0ccurences = function (list, searchElement) {
  const count = list.reduce((n, val) => n + (val === searchElement), 0);
  return count;
};
