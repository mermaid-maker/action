import { jest } from "@jest/globals";

import * as core from "../__fixtures__/core.js";

jest.unstable_mockModule("@actions/core", () => core)

const input_collector = await import("../src/input-collector.js");

test("test stuff out woo", async () => {
    core.getInput.mockImplementation((inputName) => {
        if (inputName == "input_dir") return "all";
        else if (inputName == "input_file_extension") return "mmd";
        else if (inputName == "output_dir") return "same";
        else if (inputName == "output_file_extension") return "svg";
        else return "";
    })
    core.getBooleanInput.mockImplementation((inputName) => false);
    const result = await input_collector.input_collector();

    expect(result).toStrictEqual({
        "convert_existing": false,
        "input_dir": "all",
        "input_file_extension": "mmd",
        "output_dir": "same",
        "output_file_extension": "svg"
    });
})