

fn main() {
    let my_string = String::from("hello world");

    // first_word works on slices of 'String's
    let word = first_word(&my_string[..]);

    println!("First word is: {}", word);

    let my_string_literal = "hello world";

    // Because string literals *are* string slices already,
    // this works too, without the slice sintax
    let word = first_word(my_string_literal);

    println!("First word is: {}", word);
}

fn first_word(s: &str) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[..i];
        }
    }

    &s[..]
}