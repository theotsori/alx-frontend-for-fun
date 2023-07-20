# Flexbox Layout

Flexbox is a powerful layout model in CSS that allows you to create flexible and responsive web designs. With flexbox, you can easily arrange elements within a container, distributing available space and handling alignment in an intuitive way.

![Flex box](https://i.morioh.com/200827/6b167dc9.webp)

## Basics of Flexbox

To use flexbox, you need to define a container element and set its display property to `flex`. The children of this container will then become flex items. Here's a basic example:

```css
.container {
  display: flex;
}
```

## Main Axis and Cross Axis

Flexbox operates on two axes: the main axis and the cross axis. The main axis is the primary direction in which flex items are laid out, while the cross axis is perpendicular to the main axis.

By default, the main axis is horizontal (left-to-right) unless specified otherwise. You can change the main axis direction using the `flex-direction` property:

```css
.container {
  display: flex;
  flex-direction: column; /* change to 'row' for horizontal main axis */
}
```

## Flex Items

Flex items within a container can be set to grow, shrink, or maintain their original size to distribute available space. The `flex` property is a shorthand for `flex-grow`, `flex-shrink`, and `flex-basis`.

```css
.item {
  flex: 1; /* flex-grow: 1, flex-shrink: 1, flex-basis: 0% */
}
```

In this example, the flex item will grow to fill any available space in the container equally with other items that also have a flex value of 1.

## Justify Content

The `justify-content` property controls how flex items are aligned along the main axis. It determines the spacing between and around the flex items.

```css
.container {
  display: flex;
  justify-content: space-between; /* other values: flex-start, center, flex-end, space-around, space-evenly */
}
```

## Align Items and Align Self

The `align-items` property defines how flex items are aligned along the cross axis.

```css
.container {
  display: flex;
  align-items: center; /* other values: flex-start, flex-end, baseline, stretch */
}
```

Additionally, you can use the `align-self` property on individual flex items to override the container's `align-items` property.

```css
.item {
  align-self: flex-end; /* other values: flex-start, center, baseline, stretch */
}
```

## Flex Wrap

By default, flex items will try to fit within a single line. If there's not enough space, they may shrink or overflow. You can change this behavior using the `flex-wrap` property:

```css
.container {
  display: flex;
  flex-wrap: wrap; /* other value: nowrap (default) */
}
```

With `flex-wrap: wrap`, flex items will wrap to the next line when there's not enough space on the main axis.

## Conclusion

Flexbox provides a straightforward and powerful way to create responsive layouts with CSS. By understanding and utilizing its properties, you can design dynamic and flexible web interfaces that adapt to various screen sizes and devices. It's a valuable tool for modern web development.