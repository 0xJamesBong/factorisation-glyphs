# This function takes an integer and formats it as a string with commas
def numberText(num:int):
    raw_num_str = str(num)
    num_str = '{:,}'.format(num)
    length = len(raw_num_str)
    
    # Return SVG text with different font sizes based on the number of digits in the input integer
    if length <= 10: 
        return  f'<text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" class="base" font-size="1000">{num_str}</text>'
    elif length <= 20:
        return  f'<text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" class="base" font-size="800">{num_str}</text>'
    elif length <= 30:
        return  f'<text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" class="base" font-size="600">{num_str}</text>'
    elif length <= 40:
        return  f'<text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" class="base" font-size="400">{num_str}</text>'
    else :
        # If the input integer has more than 40 digits, show only the first and last 9 digits with "..." in between, and also display the total number of digits
        first = num_str[:9]
        last = num_str[-9:]
        
        return f'''
        
        <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" class="base" font-size="400">{first}......{last}</text>
        <text x="50%" y="60%" dominant-baseline="middle" text-anchor="middle" class="base" font-size="400">Total: {length} digits</text>
        
        '''

# This function takes an SVG string and wraps it in an SVG canvas
def wrapCanvas(stuffInside):
    head = '<svg xmlns="http://www.w3.org/2000/svg" width="10000" height="10000" style="background-color:white">'
    tail = '</svg>'
    wrapped = head + '\n'+ stuffInside + '\n' + tail
    print(wrapped)
    return(wrapped)

# This function formats the input integer as SVG text, wraps it in an SVG canvas, and writes it to a file
def main(num: int):
    with open(f'./number-vanilla-drafts/num.svg', 'w') as f:
        text = draw(num)
        f.write(text)

# This function formats the input integer as SVG text and wraps it in an SVG canvas
def draw(num: int):
    num = numberText(num)
    drawing = wrapCanvas(num)
    print(drawing)
    return drawing


if __name__ == "__main__":
    main(10**42+8302+1827389+128378917289378172839+719823789172839718923789127389172389712893712893789213798132)
