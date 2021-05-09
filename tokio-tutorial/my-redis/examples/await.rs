async fn say_world() {
    println!("world");
}

#[tokio::main]
async fn main() {
    // Calling `say_world()` does not execute the body of `say_world()`.
    // Instead, it returns a future
    let op = say_world();

    // This println! comes first
    println!("hello");

    // This actually says world.
    // The type of .await is () since () is the return type of say_world()
    op.await;
}