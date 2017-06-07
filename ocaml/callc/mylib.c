#include <stdlib.h>
#include <string.h>

#include <caml/mlvalues.h>
#include <caml/alloc.h>

#define NAME ", nightblues"

CAMLprim value myfunction(value str) {
  char * str_ = String_val(str);
  int size = caml_string_length(str);
  char * res_str = malloc(size + sizeof(NAME));
  memcpy(res_str, str_, size);
  memcpy(res_str + size, NAME, sizeof(NAME));
  CAMLprim value result = caml_copy_string(res_str);
  free(res_str);
  return result;
}
