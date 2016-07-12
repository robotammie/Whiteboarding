function isAnagram(string) { 
    var unmatched = new Set();
    for (var i = 0; i < string.length; i++) {
        if (unmatched.has(string[i])) {
            unmatched.delete(string[i]);
        } else {
            unmatched.add(string[i]);
        };
    }
    if (unmatched.size > 1) {
        return false;
    } else {
        return true;
    }
}