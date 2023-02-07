package main

import (
	"os"

	qrcode "github.com/skip2/go-qrcode"
)

func main() {
	// data to be encoded in the QR code
	data := "https://www.example.com"

	// create the QR code
	err := qrcode.WriteFile(data, qrcode.Medium, 256, "qr.png")
	if err != nil {
		os.Exit(1)
	}
}
