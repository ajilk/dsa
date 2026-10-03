---
title: Snippets
---

```c++
// print space or new line based on index
" \n"[i == n]

for(int i = 0; i < n; i++) {
    cout << A[i] << " \n"[i == n];
}
```

```c++
c = c | 32      // = tolower(c)
c = c & ~32     // = toupper(c)
c = c ^ 32      // = upper -> lower, lower -> upper 
```

```c++
bool odd = n & 1;
```