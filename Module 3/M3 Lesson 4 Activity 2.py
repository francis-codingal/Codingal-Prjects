try:
    val1, val2 = eval(input("Enter two integers separated by a semicolon (e.g. 10;5): "))
    output = val1 ** val2
    print("The result is", output)

except TypeError:
    print("Mathematical operation failed due to incompatible types.")

except SyntaxError:
    print("Invalid syntax. Please use a semicolon to separate your values.")

except Exception as e:
    print("An unexpected error occurred:", e)

else:
    print("Calculation completed successfully.")

finally:
    print("Cleanup operations complete.")