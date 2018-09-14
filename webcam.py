import time
import cv2

if __name__ == '__main__':

    cap = cv2.VideoCapture(0)

    frames = 0
    start_time = time.time()
    while cap.isOpened():
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        print(frame.shape)

        if ret:
            frames += 1
            fps = frames / (time.time() - start_time)
            cv2.putText(frame, 'FPS: %.2f' % fps, (10, 20), cv2.FONT_HERSHEY_PLAIN, 1, [0, 255, 0], 1)

            cv2.imshow('Demo', frame)
            key = cv2.waitKey(1)
            if key & 0xFF == ord('q'):
                break

        else:
            break

    cap.release()
    cv2.destroyAllWindows()

