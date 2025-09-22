function Welcome(props: { name: string; color: string }) {
  return <h1 style={{ color: props.color }}>Hello {props.name}!</h1>;
}

export default Welcome;
