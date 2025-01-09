frame_with_boxes = draw_bounding_boxes(frame, recognized_faces)

        # Display the resulting frame
        cv2.imshow('Face Detection and Recognition', frame_with_boxes)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and close windows
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()