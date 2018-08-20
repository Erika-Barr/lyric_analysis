var assert = require('assert');
var tester = require('../somejavascriptfile')
describe('Array', function() {
    it('should work', function() {
       assert.equal(tester.some_test(), 'hello from test')
    });

});
